from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_entries_ip_trusted_response_400 import DeleteEntriesIpTrustedResponse400
from ...models.delete_entries_ip_trusted_response_401 import DeleteEntriesIpTrustedResponse401
from ...models.delete_entries_ip_trusted_response_403 import DeleteEntriesIpTrustedResponse403
from ...models.delete_entries_ip_trusted_response_404 import DeleteEntriesIpTrustedResponse404
from ...models.delete_entries_ip_trusted_response_500 import DeleteEntriesIpTrustedResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    ids: str,
    location: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(location, Unset):
        headers["Location"] = location

    params: dict[str, Any] = {}

    params["ids"] = ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/ip/trusted",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any,
        DeleteEntriesIpTrustedResponse400,
        DeleteEntriesIpTrustedResponse401,
        DeleteEntriesIpTrustedResponse403,
        DeleteEntriesIpTrustedResponse404,
        DeleteEntriesIpTrustedResponse500,
    ]
]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == 400:
        response_400 = DeleteEntriesIpTrustedResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = DeleteEntriesIpTrustedResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = DeleteEntriesIpTrustedResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = DeleteEntriesIpTrustedResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = DeleteEntriesIpTrustedResponse500.from_dict(response.json())

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
        DeleteEntriesIpTrustedResponse400,
        DeleteEntriesIpTrustedResponse401,
        DeleteEntriesIpTrustedResponse403,
        DeleteEntriesIpTrustedResponse404,
        DeleteEntriesIpTrustedResponse500,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: str,
    location: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any,
        DeleteEntriesIpTrustedResponse400,
        DeleteEntriesIpTrustedResponse401,
        DeleteEntriesIpTrustedResponse403,
        DeleteEntriesIpTrustedResponse404,
        DeleteEntriesIpTrustedResponse500,
    ]
]:
    """Delete Trusted IPs

     Remove the trusted IP's from the collection.

    Args:
        ids (str):
        location (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteEntriesIpTrustedResponse400, DeleteEntriesIpTrustedResponse401, DeleteEntriesIpTrustedResponse403, DeleteEntriesIpTrustedResponse404, DeleteEntriesIpTrustedResponse500]]
    """

    kwargs = _get_kwargs(
        ids=ids,
        location=location,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: str,
    location: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any,
        DeleteEntriesIpTrustedResponse400,
        DeleteEntriesIpTrustedResponse401,
        DeleteEntriesIpTrustedResponse403,
        DeleteEntriesIpTrustedResponse404,
        DeleteEntriesIpTrustedResponse500,
    ]
]:
    """Delete Trusted IPs

     Remove the trusted IP's from the collection.

    Args:
        ids (str):
        location (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteEntriesIpTrustedResponse400, DeleteEntriesIpTrustedResponse401, DeleteEntriesIpTrustedResponse403, DeleteEntriesIpTrustedResponse404, DeleteEntriesIpTrustedResponse500]
    """

    return sync_detailed(
        client=client,
        ids=ids,
        location=location,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: str,
    location: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any,
        DeleteEntriesIpTrustedResponse400,
        DeleteEntriesIpTrustedResponse401,
        DeleteEntriesIpTrustedResponse403,
        DeleteEntriesIpTrustedResponse404,
        DeleteEntriesIpTrustedResponse500,
    ]
]:
    """Delete Trusted IPs

     Remove the trusted IP's from the collection.

    Args:
        ids (str):
        location (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteEntriesIpTrustedResponse400, DeleteEntriesIpTrustedResponse401, DeleteEntriesIpTrustedResponse403, DeleteEntriesIpTrustedResponse404, DeleteEntriesIpTrustedResponse500]]
    """

    kwargs = _get_kwargs(
        ids=ids,
        location=location,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    ids: str,
    location: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any,
        DeleteEntriesIpTrustedResponse400,
        DeleteEntriesIpTrustedResponse401,
        DeleteEntriesIpTrustedResponse403,
        DeleteEntriesIpTrustedResponse404,
        DeleteEntriesIpTrustedResponse500,
    ]
]:
    """Delete Trusted IPs

     Remove the trusted IP's from the collection.

    Args:
        ids (str):
        location (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteEntriesIpTrustedResponse400, DeleteEntriesIpTrustedResponse401, DeleteEntriesIpTrustedResponse403, DeleteEntriesIpTrustedResponse404, DeleteEntriesIpTrustedResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
            location=location,
        )
    ).parsed
