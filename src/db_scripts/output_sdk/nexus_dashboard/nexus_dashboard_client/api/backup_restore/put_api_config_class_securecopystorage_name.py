from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.br_error_response import BrErrorResponse
from ...models.br_sc_error_forbidden import BrScErrorForbidden
from ...models.br_secure_copy import BrSecureCopy
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: BrSecureCopy,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/config/class/securecopystorage/{name}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, BrErrorResponse, BrScErrorForbidden]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = BrScErrorForbidden.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = BrErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = BrErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, BrErrorResponse, BrScErrorForbidden]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BrSecureCopy,
) -> Response[Union[Any, BrErrorResponse, BrScErrorForbidden]]:
    """Modify a scp/sftp remote location

    Args:
        name (str):
        body (BrSecureCopy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BrErrorResponse, BrScErrorForbidden]]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BrSecureCopy,
) -> Optional[Union[Any, BrErrorResponse, BrScErrorForbidden]]:
    """Modify a scp/sftp remote location

    Args:
        name (str):
        body (BrSecureCopy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BrErrorResponse, BrScErrorForbidden]
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BrSecureCopy,
) -> Response[Union[Any, BrErrorResponse, BrScErrorForbidden]]:
    """Modify a scp/sftp remote location

    Args:
        name (str):
        body (BrSecureCopy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BrErrorResponse, BrScErrorForbidden]]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BrSecureCopy,
) -> Optional[Union[Any, BrErrorResponse, BrScErrorForbidden]]:
    """Modify a scp/sftp remote location

    Args:
        name (str):
        body (BrSecureCopy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BrErrorResponse, BrScErrorForbidden]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
