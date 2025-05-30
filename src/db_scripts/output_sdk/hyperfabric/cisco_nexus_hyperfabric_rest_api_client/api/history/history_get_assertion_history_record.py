from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.common_rest_error import CommonRestError
from ...models.reader_assert_history_api_record_response import ReaderAssertHistoryApiRecordResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    granularity: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fabric: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    port: Union[Unset, str] = UNSET,
    assert_type: Union[Unset, str] = UNSET,
    counter_type: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["startTime"] = start_time

    params["endTime"] = end_time

    params["granularity"] = granularity

    params["limit"] = limit

    params["fabric"] = fabric

    params["device"] = device

    params["port"] = port

    params["assertType"] = assert_type

    params["counterType"] = counter_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assertions/records",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CommonRestError, ReaderAssertHistoryApiRecordResponse]]:
    if response.status_code == 200:
        response_200 = ReaderAssertHistoryApiRecordResponse.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = CommonRestError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CommonRestError.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = CommonRestError.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = CommonRestError.from_dict(response.json())

        return response_409
    if response.status_code == 429:
        response_429 = CommonRestError.from_dict(response.json())

        return response_429
    if response.status_code == 500:
        response_500 = CommonRestError.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CommonRestError, ReaderAssertHistoryApiRecordResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    granularity: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fabric: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    port: Union[Unset, str] = UNSET,
    assert_type: Union[Unset, str] = UNSET,
    counter_type: Union[Unset, str] = UNSET,
) -> Response[Union[CommonRestError, ReaderAssertHistoryApiRecordResponse]]:
    """Get the list of assertion history records

    Args:
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        granularity (Union[Unset, str]):
        limit (Union[Unset, int]):
        fabric (Union[Unset, str]):
        device (Union[Unset, str]):
        port (Union[Unset, str]):
        assert_type (Union[Unset, str]):
        counter_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ReaderAssertHistoryApiRecordResponse]]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        granularity=granularity,
        limit=limit,
        fabric=fabric,
        device=device,
        port=port,
        assert_type=assert_type,
        counter_type=counter_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    granularity: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fabric: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    port: Union[Unset, str] = UNSET,
    assert_type: Union[Unset, str] = UNSET,
    counter_type: Union[Unset, str] = UNSET,
) -> Optional[Union[CommonRestError, ReaderAssertHistoryApiRecordResponse]]:
    """Get the list of assertion history records

    Args:
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        granularity (Union[Unset, str]):
        limit (Union[Unset, int]):
        fabric (Union[Unset, str]):
        device (Union[Unset, str]):
        port (Union[Unset, str]):
        assert_type (Union[Unset, str]):
        counter_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ReaderAssertHistoryApiRecordResponse]
    """

    return sync_detailed(
        client=client,
        start_time=start_time,
        end_time=end_time,
        granularity=granularity,
        limit=limit,
        fabric=fabric,
        device=device,
        port=port,
        assert_type=assert_type,
        counter_type=counter_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    granularity: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fabric: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    port: Union[Unset, str] = UNSET,
    assert_type: Union[Unset, str] = UNSET,
    counter_type: Union[Unset, str] = UNSET,
) -> Response[Union[CommonRestError, ReaderAssertHistoryApiRecordResponse]]:
    """Get the list of assertion history records

    Args:
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        granularity (Union[Unset, str]):
        limit (Union[Unset, int]):
        fabric (Union[Unset, str]):
        device (Union[Unset, str]):
        port (Union[Unset, str]):
        assert_type (Union[Unset, str]):
        counter_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CommonRestError, ReaderAssertHistoryApiRecordResponse]]
    """

    kwargs = _get_kwargs(
        start_time=start_time,
        end_time=end_time,
        granularity=granularity,
        limit=limit,
        fabric=fabric,
        device=device,
        port=port,
        assert_type=assert_type,
        counter_type=counter_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_time: Union[Unset, str] = UNSET,
    end_time: Union[Unset, str] = UNSET,
    granularity: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    fabric: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    port: Union[Unset, str] = UNSET,
    assert_type: Union[Unset, str] = UNSET,
    counter_type: Union[Unset, str] = UNSET,
) -> Optional[Union[CommonRestError, ReaderAssertHistoryApiRecordResponse]]:
    """Get the list of assertion history records

    Args:
        start_time (Union[Unset, str]):
        end_time (Union[Unset, str]):
        granularity (Union[Unset, str]):
        limit (Union[Unset, int]):
        fabric (Union[Unset, str]):
        device (Union[Unset, str]):
        port (Union[Unset, str]):
        assert_type (Union[Unset, str]):
        counter_type (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CommonRestError, ReaderAssertHistoryApiRecordResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_time=start_time,
            end_time=end_time,
            granularity=granularity,
            limit=limit,
            fabric=fabric,
            device=device,
            port=port,
            assert_type=assert_type,
            counter_type=counter_type,
        )
    ).parsed
