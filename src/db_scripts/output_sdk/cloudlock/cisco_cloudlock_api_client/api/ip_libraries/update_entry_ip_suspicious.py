from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_entry_ip_suspicious_body import UpdateEntryIpSuspiciousBody
from ...models.update_entry_ip_suspicious_response_400 import UpdateEntryIpSuspiciousResponse400
from ...models.update_entry_ip_suspicious_response_401 import UpdateEntryIpSuspiciousResponse401
from ...models.update_entry_ip_suspicious_response_403 import UpdateEntryIpSuspiciousResponse403
from ...models.update_entry_ip_suspicious_response_404 import UpdateEntryIpSuspiciousResponse404
from ...models.update_entry_ip_suspicious_response_500 import UpdateEntryIpSuspiciousResponse500
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateEntryIpSuspiciousBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/ip/suspicious/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        UpdateEntryIpSuspiciousResponse400,
        UpdateEntryIpSuspiciousResponse401,
        UpdateEntryIpSuspiciousResponse403,
        UpdateEntryIpSuspiciousResponse404,
        UpdateEntryIpSuspiciousResponse500,
    ]
]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = UpdateEntryIpSuspiciousResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = UpdateEntryIpSuspiciousResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = UpdateEntryIpSuspiciousResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = UpdateEntryIpSuspiciousResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = UpdateEntryIpSuspiciousResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Any,
        UpdateEntryIpSuspiciousResponse400,
        UpdateEntryIpSuspiciousResponse401,
        UpdateEntryIpSuspiciousResponse403,
        UpdateEntryIpSuspiciousResponse404,
        UpdateEntryIpSuspiciousResponse500,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntryIpSuspiciousBody,
) -> Response[
    Union[
        Any,
        UpdateEntryIpSuspiciousResponse400,
        UpdateEntryIpSuspiciousResponse401,
        UpdateEntryIpSuspiciousResponse403,
        UpdateEntryIpSuspiciousResponse404,
        UpdateEntryIpSuspiciousResponse500,
    ]
]:
    """Update IP Entry

     Update the TTL expiration date, IP address, categories, and short-description.

    Args:
        id (str):
        body (UpdateEntryIpSuspiciousBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateEntryIpSuspiciousResponse400, UpdateEntryIpSuspiciousResponse401, UpdateEntryIpSuspiciousResponse403, UpdateEntryIpSuspiciousResponse404, UpdateEntryIpSuspiciousResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntryIpSuspiciousBody,
) -> Optional[
    Union[
        Any,
        UpdateEntryIpSuspiciousResponse400,
        UpdateEntryIpSuspiciousResponse401,
        UpdateEntryIpSuspiciousResponse403,
        UpdateEntryIpSuspiciousResponse404,
        UpdateEntryIpSuspiciousResponse500,
    ]
]:
    """Update IP Entry

     Update the TTL expiration date, IP address, categories, and short-description.

    Args:
        id (str):
        body (UpdateEntryIpSuspiciousBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateEntryIpSuspiciousResponse400, UpdateEntryIpSuspiciousResponse401, UpdateEntryIpSuspiciousResponse403, UpdateEntryIpSuspiciousResponse404, UpdateEntryIpSuspiciousResponse500]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntryIpSuspiciousBody,
) -> Response[
    Union[
        Any,
        UpdateEntryIpSuspiciousResponse400,
        UpdateEntryIpSuspiciousResponse401,
        UpdateEntryIpSuspiciousResponse403,
        UpdateEntryIpSuspiciousResponse404,
        UpdateEntryIpSuspiciousResponse500,
    ]
]:
    """Update IP Entry

     Update the TTL expiration date, IP address, categories, and short-description.

    Args:
        id (str):
        body (UpdateEntryIpSuspiciousBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateEntryIpSuspiciousResponse400, UpdateEntryIpSuspiciousResponse401, UpdateEntryIpSuspiciousResponse403, UpdateEntryIpSuspiciousResponse404, UpdateEntryIpSuspiciousResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateEntryIpSuspiciousBody,
) -> Optional[
    Union[
        Any,
        UpdateEntryIpSuspiciousResponse400,
        UpdateEntryIpSuspiciousResponse401,
        UpdateEntryIpSuspiciousResponse403,
        UpdateEntryIpSuspiciousResponse404,
        UpdateEntryIpSuspiciousResponse500,
    ]
]:
    """Update IP Entry

     Update the TTL expiration date, IP address, categories, and short-description.

    Args:
        id (str):
        body (UpdateEntryIpSuspiciousBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateEntryIpSuspiciousResponse400, UpdateEntryIpSuspiciousResponse401, UpdateEntryIpSuspiciousResponse403, UpdateEntryIpSuspiciousResponse404, UpdateEntryIpSuspiciousResponse500]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
